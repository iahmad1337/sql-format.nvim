import io

import sqlparse
import pynvim


def format_sql_script(text_io: io.TextIOBase) -> str:
    sql_lines: list[str] = []
    for line in text_io:
        sql_lines.append(line)
    sql_script = "\n".join(sql_lines)

    return sqlparse.format(
        sql_script,
        encoding="utf-8",
        keyword_case="upper",
        identifier_case=None,  # we don't want to change the case of names
        output_format="sql",
        reindent=True,
        space_around_operators=True,
        strip_whitespace=True,
        indent_columns=True,
        indent_width=4,
        wrap_after=80,
    )


@pynvim.plugin
class FormatPlugin(object):

    def __init__(self, nvim: pynvim.Nvim):
        self.nvim = nvim

    @pynvim.command('FormatSql', nargs='*', range='%', sync=True)
    def format_sql(self, args, rangeValue):
        firstLine, lastLine = rangeValue
        firstLine -= 1
        lastLine -= 1
        formatted_lines = format_sql_script(
            io.StringIO(
                "\n".join(self.nvim.current.buffer[firstLine:lastLine+1])
            )
        ).splitlines()
        self.nvim.current.buffer[firstLine:lastLine+1] = formatted_lines
