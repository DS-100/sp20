---
layout: home
title: Home
nav_order: 0
description: >-
    Principles and Techniques of Data Science
---

# Principles and Techniques of Data Science
{: .mb-2 }
Data 100, Spring 2020
{: .mb-0 .fs-6 .text-grey-dk-000 }

{% assign instructors = site.staffers | where: 'role', 'Instructor' %}
<div class="role">
  {% for staffer in instructors %}
  {{ staffer }}
  {% endfor %}
</div>

{% if site.announcements %}
{{ site.announcements.last }}
<!-- <a href="{{ site.baseurl }}/announcements" class="btn btn-outline fs-3">
  All Announcements
</a> -->
{% endif %}

## Important Information

- When: Tuesdays and Thursdays, 9:30am-11:00am
- Where: 150 Wheeler
- What: See the [syllabus](syllabus)
- News: We will post updates about the class on [Piazza](http://piazza.com/berkeley/spring2020/data100).

This class is listed as CS C100 (undergraduate) and CS C200A (graduate). **Be sure to register for one of these two classes**.

## Goals

- Prepare students for advanced Berkeley courses in data-management, machine learning, and statistics, by providing the necessary foundation and context
- Enable students to start careers as data scientists by providing experience working with real-world data, tools, and techniques
- Empower students to apply computational and inferential thinking to address real-world problems

## Prerequisites

While we are working to make this class widely accessible we currently require the following (or equivalent) prerequisites. **We are not enforcing prerequisites during enrollment. However, all of the prerequisties will 
be used starting very early on in the class. It is your responsibility to know the material in the prerequisites.**:

- **Foundations of Data Science**: [Data8](http://data8.org) covers much of the material in DS100 but at an introductory level. Data8 provides basic exposure to python programming and working with tabular data as well as visualization, statistics, and machine learning.
- **Computing**: _The Structure and Interpretation of Computer Programs_ ([CS 61A](http://cs61a.org)) or _Computational Structures in Data Science_ ([CS 88](https://cs88-website.github.io)). These courses provide additional background in python programming (e.g., for loops, lambdas, debugging, and complexity) that will enable DS100 to focus more on the concepts in Data Science and less on the details of programming in python.
- **Math**: _Linear Algebra_ (Math 54, [EE 16a](http://ee16a.org), or Stat89a): We will need some basic concepts like linear operators, eigenvectors, derivatives, and integrals to enable statistical inference and derive new prediction algorithms. This may be satisfied concurrently to DS100.

## About Data 100

Combining data, computation, and inferential thinking, data science is redefining how people and organizations solve challenging problems and understand their world. This intermediate level class bridges between [Data8](http://data8.org) and upper division computer science and statistics courses as well as methods courses in other fields. In this class, we explore key areas of data science including question formulation, data collection and cleaning, visualization, statistical inference, predictive modeling, and decision making.​ Through a strong emphasis on data centric computing, quantitative critical thinking, and exploratory data analysis, this class covers key principles and techniques of data science. These include languages for transforming, querying and analyzing data; algorithms for machine learning methods including regression, classification and clustering; principles behind creating informative data visualizations; statistical concepts of measurement error and prediction; and techniques for scalable data processing.
