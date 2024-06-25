# Habitats tracker
Really simple app to track amount of habitats on each day.

## Example
```python
» python main.py 16719 203
Statistic for day 22 saved successfully

Total: 16922 (+500)

Instagram: 16719 (+250)
Youtube: 203 (+250)
```

## Installation
> You need to have [poetry](https://python-poetry.org/) installed.
```
git clone https://github.com/integrityofstellar/stellarcitytracker-cli
cd stellarcitytracker-cli
poetry install
```

## Usage
First argument is amount of followers on Instagram, second is amount of followers on Youtube.
```
poetry run python main.py 16719 203
```
