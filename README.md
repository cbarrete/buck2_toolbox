# Buck2 toolbox

Small tools to improve your [Buck2](https://buck2.build/) experience.

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
