# Buck2 toolbox

Small tools to improve your [Buck2](https://buck2.build/) experience.

## How to use

The currently recommended way to use the tools from this repo is to vendor them in your own.

1. I do not provide stability guarantees (at least yet).
2. You might want to make changes to the tools, and I do not intend to cover all possible edge cases.

With that being said, you _can_ also consume this repo as an [external cell](https://buck2.build/docs/users/advanced/external_cells/). To do so, add the following to your [`.buckconfig`](https://buck2.build/docs/concepts/buckconfig/):

```ini
[cells]
toolbox = toolbox

[external_cells]
toolbox = git

[external_cell_toolbox]
git_origin = https://github.com/cbarrete/buck2_toolbox
commit_hash = <replace with a valid hash>
```

You can now e.g.

```sh
buck2 bxl toolbox//launch_json.bxl:gen -- --help
```

## Tools

### `launch_json.bxl`

This [BXL](https://buck2.build/docs/bxl/) script generates `launch.json` files with debug configurations. Those files are consumed by DAP clients to determine what binaries to run under a debugger, and how.

Basic usage:

```sh
cp $(buck2 bxl launch_json.bxl:gen -- --targets //path/to:target) .vscode/launch.json
```

For more information about available flags:

```sh
buck2 bxl launch_json.bxl:gen -- --help
```

DAP clients/editors are configured differently. For Neovim, all you need is:

```lua
require('dap').adapters.lldb = {
    type = 'executable',
    -- Must be an absolute path if `runInTerminal` is used, for some reason.
    command = vim.trim(vim.system({'which', 'lldb-dap'}):wait().stdout),
}
```
