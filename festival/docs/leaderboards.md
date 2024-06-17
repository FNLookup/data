# Leaderboards

Requirements:
- Account Logged in to epicgames.com

## Steps

- Obtain account auth code

    GET - `https://www.epicgames.com/id/api/redirect?responseType=code&clientId=ec684b8c687f479fadea3cb2ad83f5c6`

    Parameter `clientId`: ID of client. In this case, fortnitePCGameClient

- Obtain eg1 token

    POST - `https://account-public-service-prod.ol.epicgames.com/account/api/oauth/token`

    Headers:
    - `Content-Type`: `application/x-www-form-urlencoded`
    - `Authorization`: `Basic ZWM2ODRiOGM2ODdmNDc5ZmFkZWEzY2IyYWQ4M2Y1YzY6ZTFmMzFjMjExZjI4NDEzMTg2MjYyZDM3YTEzZmM4NGQ=`

    Body: (Search Parameter encoding)

    - `grant_type`: `authorization_code`
    - `code`: `authorizationCode`
    - `token_type`: `eg1`

    *for example, the body should be encoded like this: `grant_type=authorization_code&code=authorizationCode&token_type=eg1`*

- Get any leaderboard:
    
    After saving your eg1 token somewhere safe, where hackers can't see it, you can use the Events API.

    - Requirements
        - `su` value from Jam Track.
        - Your account ID
        - Instrument.

            List of instruments:
            - `Solo_Guitar`
            - `Solo_Vocals`
            - `Solo_Drums`
            - `Solo_Bass`
            - `Solo_PeripheralGuitar`
            - `Solo_PeripheralBass`
        
        - Page Number (0-4 usually)
        - Season

    - Example URL:
    
        GET `https://events-public-service-live.ol.epicgames.com/api/v1/leaderboards/FNFestival/season003_478688cf-a0c4-4401-8b59-af8dafa2820d/478688cf-a0c4-4401-8b59-af8dafa2820d_Solo_Guitar/3554e7171c554bdc8b38edb226fe6b0f?page=0&rank=0&teamAccountIds=&appId=Fortnite&showLiveSessions=false`

    - Construct:
        - Base URL: `https://events-public-service-live.ol.epicgames.com/api/v1/leaderboards/FNFestival/`
        - Path 1: `season_00[SEASON]_[EVENT ID]`
        - Path 2: `[EVENT ID]_[INSTRUMENT]`
        - Path 3: `[ACCOUNT ID]`
        - Parameters:
            - `page`: `[PAGE NUMBER]`
            - `rank`: `0`
            - `teamAccountIds`: `(empty)`
            - `appId`: `Fortnite`
            - `showLiveSeasons`: `false`
        - Headers:
            - `Accept`: `application/json`
            - `Authorization`: `Bearer [YOUR EG1 TOKEN]`

    You can also get specific entries/entries of your friends (as used by Fortnite).

    - Construct:
        - Base URL: `https://events-public-service-live.ol.epicgames.com/api/v2/games/FNFestival/leaderboards/`
        - Path 1: `season00[SEASON]_[EVENT ID]`
        - Path 2: `[EVENT ID]_[INSTRUMENT]`
        - Path 3: `scores`
        - Parameters:
            - `accountId`: `[ACCOUNT ID]`
            - `fromIndex`: `0`
            - `findTeams`: `false`
        - Headers:
            - `Content-Type`: `application/json`
            - `Authorization`: `Bearer [YOUR EG1 TOKEN]`
        - Body:
            
            This is a JSON encoded text.
            Its structure follows like this:
                
            `teams`: `[[string]]`

            Example body:

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
                        "ACCOUNT ID OF SOMEONE"
                    ]
                ]
            }
            ```

## Remarks
Fortnite will return Account IDs. To access anyone's username, use the account public service API.

`https://account-public-service-prod.ol.epicgames.com/account/api/public/account`

- Parameters:
    - `accountId`: Account ID of user (repeatable, maximum 100)
- Headers:
    - `Authorization`: `Bearer [YOUR EG1 TOKEN]`