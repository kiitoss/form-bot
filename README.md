# Form Bot

This project allows automated responses to a form.

## How to use it?

To use it, clone the repository :

```sh
git clone git@github.com:kiitoss/form-bot.git
cd form-bot
```

Then, add a `data.json` file containing a structure similar to the [`data-sample.json`](data-sample.json) file.

Then run the project using :

```sh
python3 main.py
```

## Explanation of the data.json file

The JSON object contains 2 attributes:

- url: url of the form to be filled in automatically
- instructions: a list of instructions to be performed

```json
{
  "url": "https://xxx.com",
  "instructions": [
    // page 1
    [
      {
        "selector": "button[type='submit']",
        "action": "click"
      }
    ],
    // page 2
    [
      {
        "selector": ".radio-button",
        "action": "click"
      },
      {
        "selector": "button[type='submit']",
        "action": "click"
      }
    ]
  ]
}
```

The instructions are grouped in sub-lists to visually separate the pages of a form.

## Add a new instruction

A statement can contain the following properties:

- selector: the css selector of the HTML element
- action : the action to be performed on the selected element

The possible actions are :

- click : click on the selected object
