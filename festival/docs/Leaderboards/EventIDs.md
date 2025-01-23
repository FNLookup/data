## Jam Track Event IDs

Jam Track Event IDs are the common Event IDs used in the Events Service. Their structure format is as follows:

`season00x_su`

- Replace `x` with the current season number
- For Festival Season 1, instead of `season00x` it is `evergreen`.
- `su` is the `su` field found in a Jam Track's Metadata.

## Jam Track Event Window IDs

Jam Track Event Window IDs are the common Event Window IDs used in the Events Service. Their structure format is as follows:

`su_type`

- `su` is the `su` field found in a Jam Track's Metadata.
- `type` is the leaderboard type:

### Leaderboard Types

- `Solo_Vocals`: Proprietary entries on Vocals
- `Solo_Guitar`: Proprietary entries on Lead
- `Solo_Bass`: Proprietary entries on Bass
- `Solo_Drums`: Proprietary entries on Drums
- `Solo_PeripheralGuitar`: Proprietary entries on Pro Lead
- `Solo_PeripheralBass`: Proprietary entries on Pro Bass
- `Band_Duets`: Band entries of 2 band members
- `Band_Trios`: Band entries of 3 band members
- `Band_Quad`: Band entries of 4 band members
