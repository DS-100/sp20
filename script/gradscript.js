/* Data 100/200 SP20 Grade Calculation Script */
/* Run in JS console at https://okpy.org/cal/data100/sp20/ */
N_LABS = 11
N_HWS = 9
N_VITAMINS = 4
CHECKPOINT_TOTAL = 145;
N_PROJS = 2

LAB_TOTALS = [6, 6, 14, 1, 9, 8, 5, 6, 1, 1, 1] // All autograder scores
VITAMIN_TOTALS = [6, 4, 9, 8]
HW_TOTALS = [39, 36, 23, 29, 20, 21, 1, 1, 1] // Homework 3 AG only, rest is sum; 1s for HW 7, optional, and one more presumably
PROJ_TOTALS = [87, 1]

CHECKPOINT_TOTAL = 145
// MT1_TOTAL = 90
// MT2_TOTAL = 100
FINAL_TOTAL = 1 // TODO: update this

function setupLog() {
    var el = document.querySelector('#log');
    if (!el) {
        el = document.createElement('pre');
        el.id = 'log';
        el.style.position = 'fixed';
        el.style.top = '0';
        el.style.left = '0';
        el.style.width = '100%';
        el.style.height = '100%';
        el.style.background = '#282C35';
        el.style.color = '#FFF';
        el.style.zIndex = '100000';
        document.body.append(el);
        el.addEventListener("click", function() {
            el.id = 'dead';
            el.style.display = 'none';
        });
    }
}

function log() {
    document.querySelector('#log').innerHTML += [].slice.call(arguments).join('') + '\n';
}

function s(assign, type) {
    if (!scores[assign]) return 0;
    type = type || 'total';
    var result = scores[assign][type] || 0;
    if (type === 'total') {
        return Math.max(result, scores[assign].regrade || 0);
    } else if (type === 'composition') {
        return Math.max(result, scores[assign].revision || 0);
    }
    return result;
}

function lab(num) {
    var assign;
    if (num < 10) {
        assign = 'lab0' + num;
    } else {
        assign = 'lab' + num;
    }
    return s(assign);
}

function hw(num) {
    var autogradedAssign = 'hw' + num;
    var manualAssign = autogradedAssign + 'written';
    return s(autogradedAssign) + s(manualAssign);
}

function vitamin(num) {
    var assign = 'vitamin' + num;
    return s(assign);
    // return Math.min(s(assign), VITAMIN_TOTALS[num - 3]); // first vitamin week 3
}

function project(num) {
    var autogradedAssign = 'proj' + num;
    var manualAssign = autogradedAssign + 'written';
    return s(autogradedAssign) + s(manualAssign);
}

function getNLowest(scores, n) {
    // var lowestScore = 100;
    // var secondLowestScore = 100;
    // for (var i = 0; i < scores.length; i++) {
    //     if (scores[i] < lowestScore) {
    //         secondLowestScore = lowestScore;
    //         lowestScore = scores[i];
    //     } else if (scores[i] < secondLowestScore) {
    //         secondLowestScore = scores[i];
    //     }
    // }
    // return [lowestScore, secondLowestScore];
    var cp = Array.from(scores)
    return cp.sort().slice(0, n)
}

function round(number) {
    return Math.round(number * 100) / 100.0
}

function calculateGradesForAssignmentType(type) {
    var earnedPoints = [];
    var assignmentScores = [];
    var assignmentFn;
    var pointTotals;
    //var numAssignments;
    var assignmentIndices;
    if (type === "Lab") {
        assignmentFn = lab;
        pointTotals = LAB_TOTALS;
        assignmentIndices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
    } else if (type === "Homework") {
        assignmentFn = hw;
        pointTotals = HW_TOTALS;
        assignmentIndices = [1, 2, 3, 4, 5, 6, 7, 8, 'optional'];
    } else if (type === "Vitamin") {
        assignmentFn = vitamin;
        pointTotals = VITAMIN_TOTALS;
        assignmentIndices = [1, 2, 3, 4];
    } else {
        throw "Unknown assignment type. Should be 'Lab', 'Homework', or 'Vitamin'";
    }
    for (var i = 0; i < assignmentIndices.length; i++) {
        var assignmentPoints = assignmentFn(assignmentIndices[i]);
        earnedPoints.push(assignmentPoints);
        var assignmentScore = 100.0 * assignmentPoints / pointTotals[i];
        assignmentScores.push(assignmentScore);
    }
    console.log(type);
    console.log(assignmentScores);
    var droppedScores;
    if (type === "Homework" || type === "Lab") {
        droppedScores = getNLowest(assignmentScores, 3);
    } else {
        droppedScores = getNLowest(assignmentScores, 0);
    }

    var resultsString = "";
    var averageScore = 0;
    var numDrops = droppedScores.length
    for (var i = 0; i < assignmentIndices.length; i++) {
        // assignmentScore = isNaN(assignmentScores[i]) ? hw8Score : assignmentScores[i]
        if (type === "Homework" && assignmentIndices[i] === "optional") {
            resultsString += "Opt. Homework" + ":  " + earnedPoints[i] + "/" + pointTotals[i] + ",\t\t" + round(assignmentScores[i]) + "%";
        }
        else {
            resultsString += type + " " + assignmentIndices[i] + ":\t" + earnedPoints[i] + "/" + pointTotals[i] + ",\t\t" + round(assignmentScores[i]) + "%";
        }
        if (droppedScores.includes(assignmentScores[i])) {
            resultsString += " [dropped]\n";
            droppedScores.splice(droppedScores.indexOf(assignmentScores[i]), 1);
        } else {
            resultsString += "\n";
            averageScore += assignmentScores[i];
        }
    }
    var numAssignments = assignmentIndices.length;
    averageScore = averageScore / (numAssignments - numDrops);
    resultsString += "=====\n" + type + " Average: " + round(averageScore) + "%";
    return {
        score: averageScore,
        logString: resultsString
    };
}

function calculateGrades() {
    var labs = calculateGradesForAssignmentType("Lab");
    var hws = calculateGradesForAssignmentType("Homework");
    var vitamins = calculateGradesForAssignmentType("Vitamin");

    // var projEarnedPoints = [project(1), project(2), project(3)];
    // var projScores = [];
    // var projResultsString = "";
    // for (var i = 0; i < N_PROJS; i++) {
    //     projScores[i] = 100.0 * projEarnedPoints[i] / PROJ_TOTALS[i];
    //     projResultsString += "Project " + (i + 1) + ":\t" + projEarnedPoints[i] + "/" + PROJ_TOTALS[i] + ",\t\t" + round(projScores[i]) + "%\n";
    // }
    // var projAverageScore = projScores.reduce(function(a, b) { return a + b }, 0) / N_PROJS;

    var project1 = s('proj1a') + s('proj1awritten') + s('proj1b') + s('proj1bwritten');
    var project1Score = 100 * project1 / PROJ_TOTALS[0];

    var project2 = s('proj2a') + s('proj2awritten') + s('proj2b') + s('proj2bwritten');
    var project2Score = 100 * project2 / PROJ_TOTALS[1];

    var projEarnedPoints = [project1, project2];
    var projScores = [project1Score, project2Score];
    var projResultsString = "";
    for (var i = 0; i < N_PROJS; i++) {
        projResultsString += "Project " + (i + 1) + ":\t" + projEarnedPoints[i] + "/" + PROJ_TOTALS[i] + ",\t\t" + round(projScores[i]) + "%\n";
    }
    var projAverageScore = projScores.reduce(function(a, b) { return a + b }, 0) / N_PROJS;

    projResultsString += "=====\nProject Average: " + round(projAverageScore) + "%";

    // var finalProject = s('finalProject');
    // var midterm1 = s('midterm1');
    // var midterm2 = s('midterm2');

    var final = s('final');
    var finalScore = 100 * final / FINAL_TOTAL;

    var checkpoint = s('checkpointassignment');
    var checkpointScore = 100 * checkpoint / CHECKPOINT_TOTAL;

    // var finalProjectScore = 100 * finalProject / FINAL_PROJ_TOTAL;
    // var midterm1Score = 100.0 * midterm1 / MT1_TOTAL;
    // var midterm2Score = 100.0 * midterm2 / MT2_TOTAL;
    // var attendanceScore = 100 * Math.min(s('attendance'), N_ATTENDANCE) / N_ATTENDANCE;

    var ugradScore = 0.2 * hws.score +
                     0.1 * labs.score +
                     0.05 * vitamins.score +
                     0.1 * project1Score +
                     0.15 * project2Score +
                     0.1 * checkpointScore +
                     0.3 * finalScore
    var gradScore = 0.2 * hws.score +
                    0.05 * labs.score + 
                    0.075 * project1Score +
                    0.125 * project2Score +
                    0.1 * checkpointScore +
                    0.45 * finalScore

    setupLog();
    var nameEl = document.querySelector('.user-name') || document.querySelector('.widget-user-username');
    var student = nameEl.innerHTML.trim();

    log('<strong>Data 100 Spring 2020 Score Report for ', student, '</strong>');
    log('=========================================================================');
    log();
    log();
    log('<strong>Assignments</strong>');
    log('-------------------------------------------------------------------------');
    log('<strong>Labs</strong>');
    log('------------------------------');
    log(labs.logString);
    log();
    log();
    log();
    log('<strong>Homeworks</strong>');
    log('------------------------------');
    log(hws.logString);
    log();
    log();
    log();
    log('<strong>Vitamins</strong>');
    log('------------------------------');
    log(vitamins.logString);
    log();
    log();
    log();
    log('<strong>Projects 1-2</strong>');
    log('------------------------------');
    log(projResultsString);
    log();
    log();
    log();
    log('<strong>Exams</strong>');
    log('-------------------------------------------------------------------------');
    log("Checkpoint Assignment:\t" + checkpoint + "/" + CHECKPOINT_TOTAL + ",\t" + round(checkpointScore) + "%");
    log("Final:\t\t" + final + "/" + FINAL_TOTAL + ",\t" + round(finalScore) + "%");
    log();
    log();
    log();
    log('<strong>Score Calculation</strong>');
    log('-------------------------------------------------------------------------');
    log("Your score according to the undergraduate guidelines is: " + round(ugradScore) + "%");
    log("Your score according to the graduate guidelines is: " + round(gradScore) + "%");
    log("NOTE: These scores are computed based on the policies on our website.");
    log();
    log();
    log('<strong>Disclaimer</strong>')
    log('-------------------------------------------------------------------------');
    log('This calculator is only for your reference.');
    log('Please post on Piazza if you have questions about this score calculator.');
    log();
    log();
    log('<strong>Click anywhere to close.</strong>');
}
calculateGrades();
