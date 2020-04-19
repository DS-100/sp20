/* Data 100/200 SP20 Grade Calculation Script */
/* Run in JS console at https://okpy.org/cal/data100/sp20/ */
N_LABS = 11
N_HWS = 9
N_VITAMINS = 4
N_PROJS = 2
N_ATTENDANCE = 18

LAB_TOTALS = [10, 6, 8, 1, 9, 5, 7, 11, 9, 9] // All autograder scores
VITAMIN_TOTALS = [3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3] // All graded out of 3, except Vitamin 8 graded out of 1
HW_TOTALS = [24, 35, 41, 29, 32, 38, 22, 21] // Written points: [19, 18, 35, 16, 16, 38, 7, 0], Autograder points: [5, 17, 6, 13, 16, 0, 15, 15]
PROJ_TOTALS = [46, 52, 11] // Written points: [25, 24, 11], Autograder points: [21, 28, ?]
FINAL_PROJ_TOTAL = 100
MT1_TOTAL = 90
MT2_TOTAL = 100
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
    return Math.min(s(assign), VITAMIN_TOTALS[num - 3]); // first vitamin week 3
}

function project(num) {
    var autogradedAssign = 'proj' + num;
    var manualAssign = autogradedAssign + 'written';
    return s(autogradedAssign) + s(manualAssign);
}

function getLowestTwoScores(scores) {
    var lowestScore = 100;
    var secondLowestScore = 100;
    for (var i = 0; i < scores.length; i++) {
        if (scores[i] < lowestScore) {
            secondLowestScore = lowestScore;
            lowestScore = scores[i];
        } else if (scores[i] < secondLowestScore) {
            secondLowestScore = scores[i];
        }
    }
    return [lowestScore, secondLowestScore];
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
        assignmentIndices = [3, 4, 5, 6, 9, 10, 11, 13, 14, 15];
    } else if (type === "Homework") {
        assignmentFn = hw;
        pointTotals = HW_TOTALS;
        assignmentIndices = [1, 2, 3, 4, 5, 6, 7, 8];
    } else if (type === "Vitamin") {
        assignmentFn = vitamin;
        pointTotals = VITAMIN_TOTALS;
        assignmentIndices = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15];
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
    if (type === "Homework") {
        var hw8Score = assignmentScores.pop();
        droppedScores = getLowestTwoScores(assignmentScores);
        // Drop hw8Score if it is lower than secondLowest.
        // Otherwise, it makes up for secondLowest in hw avg calculation.
        if (hw8Score < droppedScores[1]) {
            droppedScores[1] = hw8Score;
        }
        assignmentScores.push(hw8Score);
        console.log(type);
        console.log(hw8Score);
        console.log(assignmentScores);
        console.log(droppedScores);
    } else {
        droppedScores = getLowestTwoScores(assignmentScores);
    }

    var resultsString = "";
    var averageScore = 0;
    var numDrops = droppedScores.length
    for (var i = 0; i < assignmentIndices.length; i++) {
        // assignmentScore = isNaN(assignmentScores[i]) ? hw8Score : assignmentScores[i]
        resultsString += type + " " + assignmentIndices[i] + ":\t" + earnedPoints[i] + "/" + pointTotals[i] + ",\t\t" + round(assignmentScores[i]) + "%";
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

    var projEarnedPoints = [project(1), project(2), project(3)];
    var projScores = [];
    var projResultsString = "";
    for (var i = 0; i < N_PROJS; i++) {
        projScores[i] = 100.0 * projEarnedPoints[i] / PROJ_TOTALS[i];
        projResultsString += "Project " + (i + 1) + ":\t" + projEarnedPoints[i] + "/" + PROJ_TOTALS[i] + ",\t\t" + round(projScores[i]) + "%\n";
    }
    var projAverageScore = projScores.reduce(function(a, b) { return a + b }, 0) / N_PROJS;
    projResultsString += "=====\nProject Average: " + round(projAverageScore) + "%";

    var finalProject = s('finalProject');
    var midterm1 = s('midterm1');
    var midterm2 = s('midterm2');
    var final = s('final');
    var finalProjectScore = 100 * finalProject / FINAL_PROJ_TOTAL;
    var midterm1Score = 100.0 * midterm1 / MT1_TOTAL;
    var midterm2Score = 100.0 * midterm2 / MT2_TOTAL;
    var finalScore = 100 * final / FINAL_TOTAL;
    var attendanceScore = 100 * Math.min(s('attendance'), N_ATTENDANCE) / N_ATTENDANCE;

    var ugradScore = 0.15 * projAverageScore +
                     0.1 * labs.score +
                     0.2 * hws.score +
                     0.05 * vitamins.score +
                     0.1 * midterm1Score +
                     0.1 * midterm2Score +
                     Math.max(0.05 * attendanceScore + 0.25 * finalScore, 0.3 * finalScore);
    var gradScore = 0.15 * projAverageScore +
                    0.2 * hws.score +
                    0.1 * midterm1Score +
                    0.1 * midterm2Score +
                    0.15 * finalProjectScore +
                    Math.max(0.05 * labs.score + 0.25 * finalScore, 0.3 * finalScore);

    setupLog();
    var nameEl = document.querySelector('.user-name') || document.querySelector('.widget-user-username');
    var student = nameEl.innerHTML.trim();

    log('<strong>Data 100 Fall 2019 Score Report for ', student, '</strong>');
    log('=========================================================================');
    log();
    log('<strong>Attendance</strong>');
    log('-------------------------------------------------------------------------');
    log("Attendance:\t" + s('attendance') + ",\t" + round(attendanceScore) + "%");
    log("NOTE: The max attendance score is 100% (at most 18/18).");
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
    log('<strong>Projects</strong>');
    log('------------------------------');
    log("<strong>NOTE: We have not yet graded Project 3 or the Grad Project.</strong>");
    log(projResultsString);
    log();
    log("Grad Project:\t" + finalProject + "/" + FINAL_PROJ_TOTAL + ",\t" + round(finalProjectScore) + "%");
    log();
    log();
    log();
    log('<strong>Exams</strong>');
    log('-------------------------------------------------------------------------');
    log("Midterm 1:\t" + midterm1 + "/" + MT1_TOTAL + ",\t" + round(midterm1Score) + "%");
    log("Midterm 2:\t" + midterm2 + "/" + MT2_TOTAL + ",\t" + round(midterm2Score) + "%");
    log("=====\nMidterm Average: " + round((midterm1Score + midterm2Score) / 2) + "%");
    log();
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
    log("<strong>UNDERGRADUATES</strong>: Your grade will be determined by the higher of these two scores: " + round(Math.max(ugradScore, gradScore)) + "%");
    log();
    log("<strong>GRADUATES</strong>: Your grade will be the graduate score: " + round(gradScore) + "%");
    log();
    log();
    log('<strong>Disclaimer</strong>')
    log('-------------------------------------------------------------------------');
    log('This calculator is only for your reference.');
    log('It does not apply if you missed a midterm.');
    log('It does not include penalties for academic dishonesty.');
    log('Please post on Piazza if you have questions about this score calculator.');
    log();
    log();
    log('<strong>Click anywhere to close.</strong>');
}
calculateGrades();
