---
layout: page
title: Calendar
nav_exclude: true
description: The weekly event schedule.
---

# Calendar

<!-- **Note:** This is not up-to-date

Schedule data are defined as YAML [data files](https://jekyllrb.com/docs/datafiles/) following the example format in `_data/schedule`.

Multiple schedules can be rendered on a page, each with their own events and hour range.

## Weekly Schedule

{% include schedule.html data=site.data.schedule.weekly interval=30 row_height=40 %}

## Office Hours Schedule

{% include schedule.html data=site.data.schedule.office-hours interval=30 row_height=40 %}
 -->

 <div id="fullcalendar"></div>

<link rel="stylesheet" property="stylesheet" href="https://unpkg.com/@fullcalendar/core/main.css">
<link rel="stylesheet" property="stylesheet" href="https://unpkg.com/@fullcalendar/timegrid/main.css">
<script src="https://unpkg.com/@fullcalendar/core/main.min.js"></script>
<script src="https://unpkg.com/@fullcalendar/daygrid/main.min.js"></script>
<script src="https://unpkg.com/@fullcalendar/timegrid/main.min.js"></script>
<script src="https://unpkg.com/@fullcalendar/google-calendar/main.min.js"></script>

<style>
.fc table {
  margin-bottom: 0;
}
</style>
<script>
document.addEventListener('DOMContentLoaded', function() {
  new FullCalendar.Calendar(document.getElementById('fullcalendar'), {
    plugins: ['dayGrid', 'timeGrid', 'googleCalendar'],
    header: {
      left: 'title',
      right: 'today prev,next',
    },
    nowIndicator: true,
    height: 'auto',
    minTime: '09:00:00',
    maxTime: '21:00:00',
    allDaySlot: false,
    slotEventOverlap: false,
    defaultView: 'timeGridWeek',
    // THIS KEY WON'T WORK IN PRODUCTION!!!
    // To make your own Google API key, follow the directions here:
    // http://fullcalendar.io/docs/google_calendar/
    googleCalendarApiKey: 'AIzaSyDcnW6WejpTOCffshGDDb4neIrXVUA1EAE',
    // US Holidays
    eventSources: [
      {
        googleCalendarId: 'en.usa#holiday@group.v.calendar.google.com',
        className: 'holiday',
      },
    ],
  }).render();
});
</script>
