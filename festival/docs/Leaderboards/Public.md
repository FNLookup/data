## Public Leaderboard

URL: https://events-public-service-live.ol.epicgames.com/api/v1/leaderboards/:gameId/:eventId/:eventWindowId/:accountId \
Method: GET \
Auth Required: Yes (`{gameId}:profile:{accountId}:commands READ`)

## Path Parameters

`gameId`: `FNFestival` <br/>
`eventId`: [Jam Track Event Id](https://github.com/FNLookup/data/blob/main/festival/docs/Leaderboards/EventIDs.md#jam-track-event-ids) <br/>
`eventWindowId`: [Jam Track Event Window Id](https://github.com/FNLookup/data/blob/main/festival/docs/Leaderboards/EventIDs.md#jam-track-event-ids) <br/>
`accountId`: Your Account Id

## Query Parameters

`page`: 0 (0 - 4) <br/>
`rank`: 0 <br/>
`showLiveSessions`: `false` (There aren't live sessions in Fortnite Festival*) <br/>
`teamAccountIds`: Leave Blank <br/>
`appId`: `Fortnite`

### Notes

- `page`: Fortnite Festival only returns up to 5 pages of entries
- `rank`: Used if `page` and `rank` are given (e.g. 54 would still go to page 1 and start at rank 1)

## Example Response

```json
{
    "gameId": "FNFestival",
    "eventId": "season003_478688cf-a0c4-4401-8b59-af8dafa2820d",
    "eventWindowId": "478688cf-a0c4-4401-8b59-af8dafa2820d_Solo_Guitar",
    "page": 0,
    "totalPages": 5,
    "updatedTime": "2025-01-23T17:11:03.577Z",
    "entries": [
        {
            "gameId": "FNFestival",
            "eventId": "season003_478688cf-a0c4-4401-8b59-af8dafa2820d",
            "eventWindowId": "478688cf-a0c4-4401-8b59-af8dafa2820d_Solo_Guitar",
            "teamAccountIds": [
                "a9a6611829c14517a71f4bc2350bc7fe"
            ],
            "pointsEarned": 320959,
            "score": 320959,
            "rank": 1,
            "percentile": -1,
            "tokens": [],
            "teamId": "a9a6611829c14517a71f4bc2350bc7fe",
            "pointBreakdown": {
                "SCORE:1": {
                    "timesAchieved": 320959,
                    "pointsEarned": 320959
                }
            },
            "sessionHistory": [
                {
                    "sessionId": "1d09a6ac864240268d521d069d0a3f0c16CDAF0789124944B00BCBA4B59D082E",
                    "endTime": "2024-04-24T09:55:59.467Z",
                    "trackedStats": {
                        "B_SCORE": 318284,
                        "M_0_ACCURACY": 1000000,
                        "M_0_DIFFICULTY": 3,
                        "B_STARS": 5,
                        "M_0_STARS_EARNED": 6,
                        "M_0_INSTRUMENT": 0,
                        "FULL_COMBO": 1,
                        "B_BASESCORE": 318284,
                        "M_0_SCORE": 318284,
                        "B_INSTRUMENT_BONUS": 0,
                        "ACCURACY": 1000000,
                        "M_0_ID_a9a6611829c14517a71f4bc2350bc7fe": 0,
                        "SCORE": 318284,
                        "INSTRUMENT_0": 0,
                        "STARS_EARNED": 6,
                        "B_FULL_COMBO": 1,
                        "B_OVERDRIVE_BONUS": 0,
                        "DIFFICULTY": 3,
                        "B_ACCURACY": 1000000,
                        "M_0_FULL_COMBO": 1,
                        "B_MODIFIER_BONUS": 0
                    }
                }
            ],
            "unscoredSessions": [
                "05914ab960284f0e8dae437daf0f153dFCA02388C1F6423D89F819C17FF4BDC2",
            ]
        }
    ],
    "liveSessions": {}
}
```
