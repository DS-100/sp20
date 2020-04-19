# Data 100 Score Calculator

This README and script were originally written by Aman Dhar. The script was tweaked in Fall 2019 and Spring 2020 by Suraj Rampure and Daniel Zhu.


## Development Info

- okpy student pages have a global variable called `scores` where we get raw assignment scores from. These scores only have inactive okpy assignment scores, so move any 'active' assignments to 'inactive' on okpy if you want them to be included.
	- the `s` function gets raw assignment scores from the `scores` variable
	- from the instructor view, there is also a global variable called `allScores` that includes active assignment scores, but this doesn't exist student-side
- The `calculateGradesForAssignmentType` assumes 2 drops. You could probably fix this to take in a variable number of drops so the function works for projects and other assignments too.
- I haven't found a good way to get assignment point totals from okpy, so they are all hardcoded right now.
- Email me at [amandhar@berkeley.edu](mailto:amandhar@berkeley.edu) if you have questions.

## Deploy Steps

1. To deploy the script, it first needs to be hosted online where students can access it. For Spring 19, I put it on a [public Github gist](https://gist.github.com/amandhar/b5a23f0fb982233cb8bb1adde8656b4d/), though it should probably be in the class's public repo.

2. If you create the bookmarklet with the gist link directly, you will hit CORS errors. However, there are several workarounds online that give the script the right headers so it doesn't get blocked. Here are links to a couple of them:
	- [GitCDN](https://gitcdn.link/) - Changes on GitHub are reflected after a couple of hours
	- [GitHack](https://raw.githack.com/) - Gives you a development link (updates in minutes) and a production link

	Use one of these websites to generate a link for the students. Gist links to the raw script will likely have this format:
    "https://gist.github.com/GITHUB\_USERNAME/REPO\_HASH/raw/COMMIT\_HASH/script.js"
    
    **NOTE:** If you pass a link without the COMMIT\_HASH (so it ends with "/raw/script.js") the link will always point to the most recent version of the script. This is helpful for development (no need to constantly update your bookmarklet while testing) and production (fix any issues on the fly without needing to send students new links).
    
3. Now that you have a new link from GitCDN/GitHack/somebody else, construct the bookmarklet link that looks like this (but replace the old script link with your new one): 
	```
	javascript:(function(){document.body.appendChild(document.createElement('script')).src='https://gist.githack.com/amandhar/b5a23f0fb982233cb8bb1adde8656b4d/raw/sp19_data100_total_score.js';})();
    ```

4. Now, create a bookmark in your browser with the bookmarklet link from Step 3 as the URL. To run the script:
	- From the instructor view on okpy, clicking on any student's email from the dashboard should take you to "https://okpy.org/admin/course/000/student_email%40berkeley.edu". Open the bookmark from this page.
	- From the student view on okpy, open the bookmark on "https://okpy.org/cal/data100/sp19".

	In case something is not working, it should help to open the JavaScript console (on Chrome, that's View > Developer > JavaScript Console).