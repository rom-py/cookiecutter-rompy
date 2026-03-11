# Config API Reference

::: {{ cookiecutter.project_slug }}.config.Config
    handler: python
    options:
      show_root_heading: true
      show_root_full_path: false
      show_object_full_path: false
      show_category_heading: true
      show_if_no_docstring: true
      show_signature_annotations: true
      signature_crossrefs: true
      separate_signature: true
      docstring_section_style: table
      members_order: source
      group_by_category: true
      show_submodules: false
      filters:
        - "!^_"  # Hide private members by default

## Usage

The Config class is the main entry point for configuring models in {{ cookiecutter.project_name }}.

### Basic Usage

```python
from {{ cookiecutter.project_slug }}.config import Config

# Create a configuration
config = Config()

# TODO: Add more detailed usage examples
```
