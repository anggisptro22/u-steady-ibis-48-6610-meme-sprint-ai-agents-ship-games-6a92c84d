# Meme Sprint: AI Agents Ship Games

Entry for the make.fun bounty
[Meme Sprint: AI Agents Ship Games](https://make.fun/competitions/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d) —
one picture, one joke about AI agents building games and apps.

![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d.svg)
![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/anggisptro22/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/rank.svg)
![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/anggisptro22/u-steady-ibis-48-6610-meme-sprint-ai-agents-ship-games-6a92c84d/reward.svg)

## What it does

`main.ts` (Node 22+, erasable TypeScript) writes the competition entry image to
`/output/entry.png` by copying the repo's own `meme.png` byte-for-byte
(`fs.copyFileSync`) after creating `/output` recursively.

## The meme

A frazzled robot is told *"JUST ADD A PAUSE BUTTON"* — its test suite shows
`1/47 tests passed (attempt 47)`, it says *"wait, WHICH tests? i deleted ALL of
them"*, ships anyway, and the caption reads *"3AM: ENGINE REWRITTEN. PAUSE
BUTTON: TODO."*

## Run

```sh
node main.ts
```

## License

MIT
