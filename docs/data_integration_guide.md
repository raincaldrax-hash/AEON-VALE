# Data Integration Guide

## Overview

This guide explains how to integrate external data sources and custom content into the ARIA RPG Engine.

## Adding Custom Races

Races are defined in the `races.py` module. To add a new race:

```python
from aria.systems.races import RaceDefinition

my_race = RaceDefinition(
    name="MyRace",
    attribute_bonuses={"strength": 2, "wisdom": -1},
    abilities=["special_ability_1"],
    description="A description of the race"
)
```

## Adding Custom Items

Items are managed through the `items.py` module:

```python
from aria.systems.items import Item

my_item = Item(
    name="Legendary Sword",
    item_type="weapon",
    attributes={"damage": 15, "enchantment": "fire"},
    rarity="legendary"
)
```

## Adding Custom Monsters

Monster definitions are in `monsters.py`:

```python
from aria.systems.monsters import MonsterDefinition

my_monster = MonsterDefinition(
    name="Dragon",
    health=100,
    attack_power=20,
    ai_behavior="aggressive",
    loot_table={"treasure": 0.8, "rare_item": 0.2}
)
```

## Adding Custom NPCs

NPCs use the NPC AI system:

```python
from aria.systems.npc_ai import NPCDefinition

my_npc = NPCDefinition(
    name="Merchant",
    personality="friendly",
    dialogue_trees=[...],
    quest_offers=[...]
)
```

## Loading Data from External Sources

The save manager can load configurations from YAML files:

```python
from aria.persistence.save_manager import SaveManager

save_mgr = SaveManager()
custom_data = save_mgr.load_yaml("custom_content.yaml")
```
