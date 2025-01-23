## Specific Leaderboard Entries

URL: https://events-public-service-live.ol.epicgames.com/api/v2/games/:gameId/leaderboards/:eventId/:eventWindowId/scores \
Method: POST \
Auth Required: Yes (`{gameId}:profile:{accountId}:commands READ`)

## Headers

`Content-Type`: `application/json`

## Path Parameters

`gameId`: `FNFestival` <br/>
`eventId`: Jam Track Event Id <br/>
`eventWindowId`: Jam Track Event Window Id <br/>

## Query Parameters

`accountId`: Your Account ID <br/>
`fromIndex`: 0 <br/>
`findTeams`: `false` <br/>

## Example Body

```json
{
    "teams": [
        [
            "YOUR ACCOUNT ID"
        ],
        [
            "ACCOUNT ID OF FRIEND"
        ],
        [
            "ACCOUNT ID OF ANYONE"
        ]
    ]
}
```

## Example Response

```json
[
    {
        "scoreKey": {
            "gameId": "FNFestival",
            "eventId": "season007_d8b33185-f755-4050-9f08-0c83cb714305",
            "eventWindowId": "d8b33185-f755-4050-9f08-0c83cb714305_Solo_Vocals"
        },
        "teamId": "3554e7171c554bdc8b38edb226fe6b0f",
        "teamAccountIds": [
            "3554e7171c554bdc8b38edb226fe6b0f"
        ],
        "pointsEarned": 103761,
        "score": 103761,
        "rank": 251282,
        "percentile": -1,
        "pointBreakdown": {
            "SCORE:1": {
                "timesAchieved": 103761,
                "pointsEarned": 103761
            }
        },
        "sessionHistory": [
            {
                "sessionId": "962166c36d884ed188d658de13cbba1387998F8CD91A4303A0F43B9AEE967AA9",
                "endTime": "2025-01-14T16:03:22.091Z",
                "trackedStats": {
                    "B_SCORE": 103761,
                    "SCORE": 103761,
                    "M_0_ACCURACY": 990000,
                    "M_0_DIFFICULTY": 3,
                    "B_STARS": 4,
                    "M_0_STARS_EARNED": 6,
                    "M_0_INSTRUMENT": 2,
                    "FULL_COMBO": 0,
                    "M_0_SCORE": 103761,
                    "SEASON": 7,
                    "B_INSTRUMENT_BONUS": 0,
                    "ACCURACY": 990000,
                    "INSTRUMENT_0": 2,
                    "STARS_EARNED": 6,
                    "B_FULL_COMBO": 0,
                    "B_OVERDRIVE_BONUS": 0,
                    "DIFFICULTY": 3,
                    "B_ACCURACY": 990000,
                    "M_0_FULL_COMBO": 0,
                    "B_MODIFIER_BONUS": 0,
                    "B_BASESCORE": 103761,
                    "M_0_ID_3554e7171c554bdc8b38edb226fe6b0f": 0
                }
            }
        ],
        "unscoredSessions": []
    }
]
```
