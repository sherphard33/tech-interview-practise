Task;
// Scheduling is how the processor decides which jobs (processes) get to use the processor and for how long. This can cause a lot of problems. For example, a long-running process might use the entire CPU and block all the other processes from executing. One solution is Shortest Job First (SJF), which you will implement in this challenge.

// SJF works by letting the shortest jobs take the CPU first. If the jobs are the same size then break the tie with First In First Out (FIFO). The idea is that the shorter jobs will finish quicker, so theoretically jobs won't get frozen because of large jobs. (In practice they're frozen because of small jobs).

// Specification
// sjf(jobs, index)
// Returns the clock-cycles (cc) of when the process will be executed for a given index

// Parameters
// jobs: Array<Integers> - A non-empty array of positive integers representing the clock cycles needed to finish a job.

// index: number - A positive integer that respresents the job we're interested in

// Return Value
// number - A number representing the clock cycles it takes to complete the job at index.

const sjf = (jobs, index) => {
  let sorted = jobs.sort((a, b) => a - b);
  const time = sorted.slice(0, index).reduce((a, b) => a + b, 0);
  return time;
};

const sjf = (jobs: Array<number>, index: number): number => {
  // declare waiting time array
  var waitingTime: any = [];
  // set waiting time for first task to zero
  waitingTime[0] = 0;

  // declare total time array
  var totalTimeArray: any = [];

  var processArray: any = [];
  // add job value and index as an object to process array
  for (let i: number = 0; i < jobs.length; i++) {
    processArray.push({
      id: i,
      value: jobs[i],
    });
  }

  // sort the array in ascending order
  function sortArray(a: any, b: any) {
    return a.value - b.value;
  }

  // calculate waiting time for each process except first process
  // waiting time for first process is zero so we start to calculate from index 1
  function calculateWaitingTime(sortedArray: any[], waitingTime: number[]) {
    for (let i: number = 1; i < sortedArray.length; i++) {
      waitingTime.push(sortedArray[i - 1].value + waitingTime[i - 1]);
    }
  }

  // total time taken to complete each task
  function calculateTimeForEachTask(sortedArray: any[], totalTimeArray: any[]) {
    for (let i: number = 0; i < sortedArray.length; i++) {
      totalTimeArray.push({
        id: sortedArray[i].id,
        time: sortedArray[i].value + waitingTime[i],
      });
    }
  }

  // find clock cycles
  function findClockCycles(totalTimeArray: any[], index: number) {
    for (let i: number = 0; i < totalTimeArray.length; i++) {
      if (totalTimeArray[i].id === index) {
        return totalTimeArray[i].time;
      }
    }
  }

  // First of all sort the process array in ascending order of their value
  var sortedArray = processArray.sort(sortArray);

  // calculate waiting time for the rest of the processes
  calculateWaitingTime(sortedArray, waitingTime);

  // calculate total time for each task
  calculateTimeForEachTask(sortedArray, totalTimeArray);

  // return clock cycles for the task
  return findClockCycles(totalTimeArray, index);
};
