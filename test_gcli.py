from click.testing import CliRunner
from cli import hello
from search import clisearch 

def test_hello():
  runner = CliRunner()
  result = runner.invoke(hello, [])
  assert result.exit_code == 0
  assert 'Hello' in result.output

def test_clisearch():
  runner = CliRunner()
  result = runner.invoke(clisearch, ['--path', '.', '--ftype', 'py'])
  assert result.exit_code == 0
  assert '.py' in result.output