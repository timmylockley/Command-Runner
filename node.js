const { spawn } = require("child_process");

// Pick a command to demonstrate. "ping" works well because it runs forever.
const isWindows = process.platform === "win32";
const command = isWindows ? "ping" : "ping";
const args = isWindows ? ["-t", "127.0.0.1"] : ["127.0.0.1"];

console.log("Starting:", command, args.join(" "));

// Spawn the child process
const child = spawn(command, args, {
  stdio: "inherit"     // show its output in your terminal
});

// After a delay, send Ctrl+C (SIGINT)
const delayMs = 3000; // 3 seconds
setTimeout(() => {
  console.log("\nSending Ctrl+Shift+Q+Q (SIGINT) to child process...");
  // This is the actual Ctrl+C signal.
  child.kill("SIGINT");
}, delayMs);

// When the child exits, report why
child.on("exit", (code, signal) => {
  console.log(`\nChild exited. Code=${code}, Signal=${signal}`);
});
