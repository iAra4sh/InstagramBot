## InstagramBot
This script can like posts related to a specific hashtag or unfollow your followings.
> ***Please read the tips carefully before using.***

## tip 
1. You do not need to log in to your Instagram account manually, just enter your username and password in the script to log in to your user account.
2. If 2-step verification is enabled on your account, the script will not run properly.
3. If you are using a proxy or VPN, the script may be compromised.
4. Make sure File [ myig.py ] and File [chromedriver.exe] are in the same direction.


## Usage
| Command | Description | Example
| --- | --- | --- |
| `--like` | Like a hashtag posts | myig.py --like animal |
| `--unfollow` | Unfollow page followings | myig.py --unfollow 10 |

### what is Scroll Count ?
That is, it scrolls the page to the number you enter and collects post links to like.
The more you enter, the more links will be collected for likes and the script will open those links one by one and like the post.
It also stores links in a text file called **Posts_Link.txt** .

## Requirements
- You must have **Python version 3.8.5** or higher installed on your computer.
- To add some essential libraries to the path where the " Requirement.txt " file is located , Enter the " pip install -r requirement.txt " command on the command line.
- You must have Google Chrome version 87.0.4280.66 installed on your computer.
- It is better to use Cmder software to run on Windows.
