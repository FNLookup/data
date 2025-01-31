## Public Leaderboards - Event Window History

URL: https://events-public-service-live.ol.epicgames.com/api/v1/events/:gameId/:eventId/:eventWindowId/history/:accountId \
Method: GET \
Auth Required: Yes (`{gameId}:profile:{accountId}:commands READ`)

## Path Parameters

`gameId`: `FNFestival` <br/>
`eventId`: [Jam Track Event ID](https://github.com/FNLookup/data/blob/main/festival/docs/Leaderboards/EventIDs.md#jam-track-event-ids) <br/>
`eventWindowId`: [Jam Track Event Window ID](https://github.com/FNLookup/data/blob/main/festival/docs/Leaderboards/EventIDs.md#jam-track-event-window-ids) <br/>
`accountId`: Your account ID

## Example Response

```json
[
    {
        "scoreKey": {
            "gameId": "FNFestival",
            "eventId": "season006_f3ca1e87-a1d6-4a48-8140-9d9b2ba48201",
            "eventWindowId": "f3ca1e87-a1d6-4a48-8140-9d9b2ba48201_Solo_Vocals"
        },
        "teamId": "3554e7171c554bdc8b38edb226fe6b0f",
        "teamAccountIds": [
            "3554e7171c554bdc8b38edb226fe6b0f"
        ],
        "pointsEarned": 138345,
        "score": 138345,
        "rank": 10493,
        "percentile": 0.07661025363958938,
        "pointBreakdown": {
            "SCORE:1": {
                "timesAchieved": 138345,
                "pointsEarned": 138345
            }
        },
        "sessionHistory": [
            {
                "sessionId": "7ba07ccc1b1b44a7a9d6c3518f70df4e98042B6030CA40D2B013E550BAD1EBED",
                "endTime": "2025-01-10T22:31:33.564Z",
                "trackedStats": {
                    "B_SCORE": 138345,
                    "SCORE": 138345,
                    "M_0_ACCURACY": 990000,
                    "M_0_DIFFICULTY": 3,
                    "B_STARS": 5,
                    "M_0_STARS_EARNED": 6,
                    "M_0_INSTRUMENT": 2,
                    "FULL_COMBO": 0,
                    "M_0_SCORE": 138345,
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
                    "B_BASESCORE": 138345,
                    "M_0_ID_3554e7171c554bdc8b38edb226fe6b0f": 0
                }
            }
        ],
        "unscoredSessions": []
    }
]
```
