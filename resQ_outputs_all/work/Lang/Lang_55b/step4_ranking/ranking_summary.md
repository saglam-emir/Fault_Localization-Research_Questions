# Ranking Comparison Summary

Ground truth faulty statement(s) (diff line): [('StopWatch.java', 118), ('StopWatch.java', 119)]

Ground_Truth_Answerable: True

- SBFL   ranked 154 statement(s)
- Hybrid ranked 7 statement(s)

## Top 10 - Trace-Based SBFL

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | StopWatch.java:179 | 0.707107 | `stopTime = System.currentTimeMillis();` |
| 1 | 2 | StopWatch.java:180 | 0.707107 | `this.runningState = STATE_SUSPENDED;` |
| 3 | 1 | StopWatch.java:176 | 0.57735 | `if(this.runningState != STATE_RUNNING) {` |
| 4 | 1 | StopWatch.java:210 | 0.5 | `return this.stopTime - this.startTime;` |
| 5 | 4 | StopWatch.java:115 | 0.447214 | `if(this.runningState != STATE_RUNNING && this.runningState != STATE_SUSPENDED) {` |
| 5 | 4 | StopWatch.java:118 | 0.447214 | `stopTime = System.currentTimeMillis();` |
| 5 | 4 | StopWatch.java:119 | 0.447214 | `this.runningState = STATE_STOPPED;` |
| 5 | 4 | StopWatch.java:209 | 0.447214 | `if(this.runningState == STATE_STOPPED || this.runningState == STATE_SUSPENDED) {` |
| 9 | 10 | StopWatch.java:65 | 0.408248 | `private int runningState = STATE_UNSTARTED;` |
| 9 | 10 | StopWatch.java:70 | 0.408248 | `private int splitState   = STATE_UNSPLIT;` |

## Top 10 - Slice-Based Hybrid

| Rank | Tie Size | File:Line | Ochiai | Code |
|------|----------|-----------|--------|------|
| 1 | 2 | StopWatch.java:118 | 1.0 | `stopTime = System.currentTimeMillis();` |
| 1 | 2 | StopWatch.java:119 | 1.0 | `this.runningState = STATE_STOPPED;` |
| 3 | 5 | StopWatch.java:103 | 0.57735 | `startTime = System.currentTimeMillis();` |
| 3 | 5 | StopWatch.java:179 | 0.57735 | `stopTime = System.currentTimeMillis();` |
| 3 | 5 | StopWatch.java:180 | 0.57735 | `this.runningState = STATE_SUSPENDED;` |
| 3 | 5 | StopWatch.java:209 | 0.57735 | `if(this.runningState == STATE_STOPPED || this.runningState == STATE_SUSPENDED) {` |
| 3 | 5 | StopWatch.java:210 | 0.57735 | `return this.stopTime - this.startTime;` |

