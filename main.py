import falcon


class GlobalResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        # quote = {
        #     'quote': (
        #         "I've always been more interested in "
        #         "the future than in the past."
        #     ),
        #     'author': 'Grace Hopper'
        # }

        quote = {
            "bugReportURL": "mailto:support+ancientsrevival@anashidgames.com",
            "downloadURL": "https://cafebazaar.ir/app/com.anashidgames.ancientsrevivial/?l=fa",
            "latestVersion": "0.30.1604",
            "telegramChannel": "https://t.me/Anashidgames",
            "apTakenDamage": 1,
            "apDeath": 2,
            "initialCoin": 250,
            "tcpServerIPAddress": "138.201.63.209",
            "httpServerIPAddress": "http://138.201.63.209",
            "tcpServerPortNumber": 9092,
            "httpServerPortNumber": 8000,
            "timeToGemFormula": "{0} / 300",
            "leagueTypeToUnlock": "cooper",
            "leagueStepToUnlock": 1,
            "troopScoreDeath": 2,
            "heroScoreDeath": 10,
            "registerAccountReward": 100,
            "inMaintenance": False,
            "pingProblemNumber": 2.5
        }

        resp.media = quote


api = falcon.API()
api.add_route('/global', GlobalResource())
