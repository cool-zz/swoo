"Captchas are for the lazy and uninspired." -- some stupid asshole

Requirements
==============
- Python 2.6+ (modules: requests, socks.py [included in repo])
- phantomjs (1.9.2) and casperjs (1.1.0)
- SOCKS 5 proxies

Usage
=====
- Add proxies to proxies.txt
- From the command line, run "python supwoo.py"
- That's it

Features
========
- Auto-purges dead/banned proxies from proxies.txt
- Gathers threads from last page of /wooo/ to ensure that only dead/outdated threads are bumped
- Uses multiprocessing to give each proxy a process for posting

Notes
=====
- Only tested on Linux 32 bit, but should work with other platforms/architectures which meet the dependency requirements
- Please do not abuse this script, I would hate for the denizens of 420chan.org to suffer any inconvenience from  misue of this script :(
- If you have any questions, join irc.hardchats.com #dadfuckers or tweet me @coolchatter
