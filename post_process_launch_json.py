import json
import sys

with open(sys.argv[1]) as f:
    raw = json.load(f)

# When deriving the command line from `ExternalTestRunnerInfo`, the program is
# coerced from a `cmd_args`, which gets serialized as a list.
# Unwrap it.
for config in raw["configurations"]:
    if "program" not in config:
        continue
    assert not "argv" in config
    program = config["program"]
    if isinstance(program, list):
        assert len(program) == 1
        config["program"] = program[0]

# When deriving the command line from `RunInfo`, the whole command line is
# coerced from a single `cmd_args`. It cannot be split in BXL, so it is passed
# as a single (non-standard) `argv` list.
# Split it between `program` and `args`.
for config in raw["configurations"]:
    argv = config.pop("argv", None)
    if argv:
        assert not "program" in config
        assert not "args" in config
        config["program"] = argv[0]
        config["args"] = argv[1:]

with open(sys.argv[2], "w") as f:
    json.dump(raw, f, indent=4)
    f.write("\n")
