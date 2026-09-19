import json
import sys

with open(sys.argv[1]) as f:
    raw = json.load(f)

# When deriving the command line from `ExternalTestRunnerInfo`, the program is
# coerced from a `cmd_args`, which gets serialized as a list.
# Unwrap it.
for config in raw["configurations"]:
    program = config["program"]
    if isinstance(program, list):
        assert len(program) == 1
        config["program"] = program[0]

with open(sys.argv[2], "w") as f:
    json.dump(raw, f, indent=4)
    f.write("\n")
