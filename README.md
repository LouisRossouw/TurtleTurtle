# TurtleTurtle

an old experimental project for trading crypto that would run on my Raspberry Pi.

My bots would buy and sell on Valr exchange, based off a bunch of indicators including Exponential Moving Averages and Linear regression. the bots can also be brute force backtested on historical data.

Telegram app was used to recieve notifications from the bots and whale movements, and the bots were controllable by sending commands via telegram app.

I last worked on this project about 9 months ago and i was re-structuring the project so i dont think it works properly anymore, but at some point i plan on working on it again, would like to try arbitrage and build Kucoin bots.

Does it make money? Not really! its really hard to try predict the markets direction, however i do think its profitable when the market moves sideways and trading very volatile coins. however money aside, it was a very fun project to try build and i renjoyed watching it "do things".

----------------------------------------------------------------------------------------------------

- backtesting on collected historical data to fine tweak the bots.  
<p align="center">
<img src="https://user-images.githubusercontent.com/80905013/193472741-b1263735-a187-4d36-aff3-7bb83ab63270.gif" align="center" width="100%">
</p>

- Dots are entry and exit points, green is short term Linear regression, pink is a more long term Linear regression, red and blue lines are bid and buy SMA, yellow is a   longer EMA.


- Telegram bot to recieve notifications on whale activity and potential Arbitrage oppertunities. also could send commands to specific bots to force exit sales or hold.
<p align="center">
<img src="https://user-images.githubusercontent.com/80905013/193473119-0542ffd9-454e-488f-a904-ffa58f868fc5.PNG" align="center" width="50%">
</p>
