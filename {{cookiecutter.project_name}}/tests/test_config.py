from importlib.metadata import entry_points
from {{ cookiecutter.project_slug }}.config import Config


def test_config_entrypoint():
    eps = entry_points(group="rompy.config")
    names = [ep.name for ep in eps]
    assert "{{ cookiecutter.model_name }}" in names