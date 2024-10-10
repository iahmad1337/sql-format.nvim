# FormatSql
Plugin that introduces a `:FormatSql` command, that acts on ranges.
If no range is supplied (e.g. via visual selection), the whole file is formatted

# Use
In packer.nvim:
```
    use 'iahmad1337/sql-format.nvim'
```
And do `:PackerUpdate` or `:PackerSync`

# Requierements
- nvim that supports remote plugins
- python3.9+

Also some libs:
```shell
pip3 install pynvim sqlparse
```

# Debug
```vimscript
" Info about command definition
:command FormatSql

# Update the plugins
UpdateRemotePlugins
```
