## Player History - All Event Windows Ever Played

URL: https://events-public-service-live.ol.epicgames.com/api/v1/events/:gameId/download/:accountId \
Method: GET
Auth Required: Yes (`{gameId}:profile:{accountId}:commands READ`)

## Path Parameters

`gameId`: `FNFestival` <br/>
`accountId`: Your Account ID

## Query Parameters

`region`: required, `NULL` <br/>
`platform`: required, `null` <br/>
`teamAccountIds`: required, your account ID

## Example Response (shortened)

```json
{
    "player": {
        "tokens": [
            "FestivalPlayer"
        ],
        "gameId": "FNFestival",
        "accountId": "3554e7171c554bdc8b38edb226fe6b0f",
        "teams": {
            "season003_fc739d6a-98cc-4936-9626-594dcd09be1b:fc739d6a-98cc-4936-9626-594dcd09be1b_Solo_Guitar": [
                "3554e7171c554bdc8b38edb226fe6b0f"
            ],
            "season006_912f6323-5761-422e-85b8-42f1058d8d5a:912f6323-5761-422e-85b8-42f1058d8d5a_Band_Duets": [
                "3554e7171c554bdc8b38edb226fe6b0f"
            ],
            "evergreen_e8553a7c-d608-465d-8750-aa90a15cbec2:e8553a7c-d608-465d-8750-aa90a15cbec2_Solo_Drums": [
                "3554e7171c554bdc8b38edb226fe6b0f"
            ]
        },
        "pendingPayouts": [
            "season003_fc739d6a-98cc-4936-9626-594dcd09be1b:fc739d6a-98cc-4936-9626-594dcd09be1b_Solo_Guitar",
            "season006_912f6323-5761-422e-85b8-42f1058d8d5a:912f6323-5761-422e-85b8-42f1058d8d5a_Band_Duets",
            "evergreen_e8553a7c-d608-465d-8750-aa90a15cbec2:e8553a7c-d608-465d-8750-aa90a15cbec2_Solo_Drums"
        ],
        "pendingPenalties": {},
        "persistentScores": {},
        "groupIdentity": {}
    },
    "scoringRuleSets": {},
    "payoutTables": {},
    "events": [],
    "templates": [],
    "scores": [],
    "leaderboardDefs": [],
    "scoreLocationScoringRuleSets": {},
    "scoreLocationPayoutTables": {},
    "resolvedWindowLocations": {},
    "eventSeries": []
}
```
