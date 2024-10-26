## Development

```bash
python3 -m pip install --user pipx
pipx install pdm
pdm install
pdm install -g ci-quality
pdm run pre-commit install
```

or simply run make install which will execute the above commands.
```bash
make install
```
