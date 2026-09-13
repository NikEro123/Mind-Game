# The Mind

A small desktop puzzle game built with Python and Tkinter.

Four buttons appear, each showing a random number between 1 and 50 and coloured either
red or cyan. Click them in an order that satisfies both rules at once:

- **Red numbers** must land in **descending** order
- **Cyan numbers** must land in **ascending** order

You get four lives. Every click sends its number onto the matching stack, drawn as
overlapping cards on one of the two canvases. Get all four placed correctly and you win.

## Run it

```bash
python train.py
```

No dependencies — Tkinter ships with Python.

## How it works

**Screens are frames that get packed and unpacked.** The start screen, the game table
and the result screen are separate Tkinter frames; switching views is `pack()` and
`pack_forget()` rather than opening new windows. Simple, and it keeps one window for the
whole game.

**Buttons carry their own state.** Rather than tracking which number and colour belongs
to which button in a separate structure, `click()` reads them straight off the widget
with `button.cget("text")` and `button.cget("fg")`, then routes the number to the right
stack.

**The stacks are drawn, not listed.** `draw()` clears its canvas and redraws every card
from scratch, offsetting each one by 10px so they overlap like a hand of cards. Redrawing
the whole canvas each time is less code than tracking individual card objects, and at
four cards the cost is nothing.

**Win checking is two `all()` expressions** — one asserting each red number is greater
than the next, one asserting each cyan number is smaller than the next.

## What I learned

- Tkinter layout with frames, and switching "screens" by packing and unpacking them
- Drawing on a `Canvas` with `create_rectangle` and `create_text`, and why you clear
  before redrawing
- `window.after()` for delayed actions — showing "Try again!" for two seconds before
  resetting the board
- Passing arguments to button callbacks with `lambda`, and why `command=click(button)`
  would fire immediately while `command=lambda: click(button)` doesn't
- That reading state off widgets works, but gets fragile fast — see below

## Known limitations

- The four colours are chosen once when the program starts, so a restart always deals the
  same colour pattern. They should be re-randomised in `restart()`.
- Game state lives in module-level globals (`red_nums`, `blue_nums`, `lives`,
  `result_label`) rather than in a class. It works at this size, and it's the first thing
  I'd restructure if the game grew.
- No score tracking, and no way to undo a misclick.
- The UI is built at module level instead of inside a `GUI` class the way I structured my
  [2048 game](https://github.com/NikEro123/2048-Game) — that project came later and the
  separation is cleaner there.
