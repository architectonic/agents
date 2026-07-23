import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";

const root = path.resolve(import.meta.dirname, "..");
const temp = fs.mkdtempSync(path.join(os.tmpdir(), "architectonic-agents-pack-"));
const run = (command, args, cwd = root) =>
  spawnSync(command, args, { cwd, encoding: "utf8", stdio: "pipe" });

const required = [
  "AGENTS.md",
  "architectonic.protocol.json",
  "archetypes/operator/agent.bundle.json",
  "dist/catalog.json",
  "dist/install-manifest.json",
  "doctrine/agents.md",
  "operations/ledger.json",
  "schema/agent.schema.json",
  "schema/install-spec.schema.json",
  "specializations/brazilian-tax-law/knowledge-set.md",
  "templates/installed-agent/agent.md",
];

try {
  const npmExecPath = process.env.npm_execpath;
  const packed = npmExecPath
    ? run(process.execPath, [npmExecPath, "pack", "--pack-destination", temp])
    : run(process.platform === "win32" ? "npm.cmd" : "npm", ["pack", "--pack-destination", temp]);
  if (packed.status !== 0) throw packed.error || new Error(packed.stderr || packed.stdout);

  const archive = packed.stdout.trim().split(/\r?\n/).filter(Boolean).pop();
  const extracted = run("tar", ["-xzf", path.join(temp, archive), "-C", temp]);
  if (extracted.status !== 0) throw extracted.error || new Error(extracted.stderr || extracted.stdout);

  const packageRoot = path.join(temp, "package");
  const missing = required.filter((relativePath) => !fs.existsSync(path.join(packageRoot, relativePath)));
  if (missing.length) throw new Error(`packed package is missing: ${missing.join(", ")}`);

  console.log(`packed agents package contains ${required.length} required contract artifacts`);
} finally {
  fs.rmSync(temp, { recursive: true, force: true });
}
