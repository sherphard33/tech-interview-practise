/*Two Number Sum
Write a function that takes in a non-empty array of distinct intergers and an integer representing a target sum.
If any two numbers in the input array sum up to the target sum, the function should return them in an array, in any order. If no
two numbers sum up to the targetSum , the function should return an empty array.
*/
//array = [3, 5, -4, 8, 11, 1, 2, 6];
//targetSum = 10;

const twoNumSum = (arr, tSum) => {
  const len = arr.length - 1;
  let memo = {};
  for (let i = 0; i < len; i++) {
    let num1 = arr[i];
    let num2 = tSum - num1;
    if (num2 in memo) {
      return [num1, num2];
    } else {
      memo[num1] = "another number";
    }
  }
  return [];
};

/* Given two non empty arrays of integers, write a function that determines whether
the second array is a subsequence of the first */

//array = [5, 1, 22, 25, 6, -1, 8, 10];
//sequence = [1, 6, -1, 10];

const vailSeq = (arr, seq) => {
  let idx = 0;
  let len = arr.length;
  for (let i = 0; i < len; i++) {
    let value = arr[i];
    if (idx == seq.length) {
      return true;
    }
    let seqNum = seq[idx];
    if (seqNum == value) {
      idx++;
    }
  }
  return idx == seq.length;
};

/*
Write a function that takes in non-empty array of intergers that are sorted in ascending order and
returns a new array of the same length with the squares of te original intergers also sorted in ascending order.
*/

//array = [-4, -1, 5, 6, 8, 10, 22, 25];

const array_sorter = (arr) => {
  // Write your code here.
  const len = arr.length;
  const newArr = [];
  for (let i = 0; i < len - 1; i++) {
    let newValue = arr[i] ** 2;
    newArr.push(newValue);
  }
  let sortedArray = newArr.sort(function (a, b) {
    return a - b;
  });
  return sortedArray;
};

//Minimum waiting waiting time

const minWaitingTime = (arr) => {
  const len = arr.length;
  let totalWaitingTime = 0;
  arr.sort(function (a, b) {
    return a - b;
  });
  for (let idx = 0; idx < len; idx++) {
    let eRemaining = len - (idx + 1);
    totalWaitingTime += arr[idx] * eRemaining;
  }
  return totalWaitingTime;
};

//array2 = [3, 2, 1, 2, 6];

const longArr = (arr) => {
  let memo = new Set();
  let sml = 0;
  let res = 0;
  for (let i = 0; i < arr.length; i++) {
    while (memo.has(arr.charAt(i))) {
      console.log("found dublicate", arr.charAt(i));
      memo.delete(arr.charAt(sml));
      sml++;
    }
    memo.add(arr[i]);
    //console.log("added next one", arr[i]);
    res = Math.max(res, i - sml + 1);
  }
  return res;
};
s = "abcabcbb";

const gWord = "mamma";
const hWord = "maxim";

//Woddle code
const colorizeWordle = (guessedWord, hiddenWord) => {
  let result = "";
  let memo = {};
  for (let i = 0; i < guessedWord.length; i++) {
    let guessLetter = guessedWord.charAt(i);
    let hiddenLetter = hiddenWord.charAt(i);

    if (guessLetter === hiddenLetter) {
      result += "G";
      memo[guessedWord.charAt(i)] = "G";
    } else if (
      memo[guessedWord.charAt(i)] !== "Y" &&
      hiddenWord.indexOf(guessLetter) != 1
    ) {
      result += "Y";
      memo[guessedWord.charAt(i)] = "Y";
    } else {
      result += "B";
    }
  }
  return result;
};

console.log(colorizeWordle(gWord, hWord));

const checkMemo = (gWords) => {
  memo = {};
  result = "";
  for (let i = 0; i < gWords.length; i++) {
    console.log(gWords.charAt(i));
    if (!(gWords.charAt(i) in memo)) {
      memo[gWords.charAt(i)] = "another1";
    }
  }
  return memo;
};

// Buffering Promises
// In this challenge, you'll be asked to wrap an unknown asynchronous function, returning a new function with a modified asynchronous behavior.
// The returned function will prevent making too many calls to the asynchronous function at once by buffering extra requests until an earlier one has completed.
// A common use case would be to prevent overrunning an API endpoint, so you make no more than 4 requests simultaneously.
// Your Task
// Modify the bufferPromise function to enable calling up to a maxActive times to our external deferred process, buffering any more requests until we have less than maxActive requests running.
const bufferPromise = (promiseFactoryFn, maxActive = 5) => {
  // Keeps track of the number of currently running tasks
  let activeCount = 0;

  // Keeps track of waiting tasks (in the format { args, resolve, reject })
  const queue = [];
  // Enqueue the task or run it immediately
  const enqueueTask = (task) => {
    // If activeCount is less than maxCount
    // We can run more tasks than we do now
    if (activeCount < maxActive) {
      // Increase the counter
      activeCount++;

      // Start the new task immediately
      startTask(task);

      // We are running as many tasks as we can
    } else {
      // Put this new task into the queue
      queue.push(task);
    }
  };

  // Start the task
  const startTask = (task) => {
    // Run the async funtion
    promiseFactoryFn(task.args)
      // If successful resolve our promise as well
      .then(task.resolve)

      // If unsuccessful reject our promise as well
      .catch(task.reject)

      // When the task finishes (fails or succeeds) try to start the next task
      .finally(startNextTask);
  };

  // Tries to start the next task in the queue
  const startNextTask = () => {
    // Get the first element of an array
    const nextTask = queue.shift();

    // If it's truey
    // There is actually another task to run
    if (nextTask) {
      // Start that task
      startTask(nextTask);

      // There is no other task to run
    } else {
      // Decrease the counter
      activeCount--;
    }
  };

  // Return a funtion
  // which creates the task object and enqueues it
  // and wraps it all up in a promise
  return (args) =>
    new Promise((resolve, reject) => enqueueTask({ args, resolve, reject }));
};

//Task;
// Scheduling is how the processor decides which jobs (processes) get to use the processor and for how long. This can cause a lot of problems.
//For example, a long-running process might use the entire CPU and block all the other processes from executing. One solution is Shortest Job First (SJF), which you will implement in this challenge.
// SJF works by letting the shortest jobs take the CPU first. If the jobs are the same size then break the tie with First In First Out (FIFO).
//The idea is that the shorter jobs will finish quicker, so theoretically jobs won't get frozen because of large jobs. (In practice they're frozen because of small jobs).
// Specification
// sjf(jobs, index)
// Returns the clock-cycles (cc) of when the process will be executed for a given index
// Parameters
// jobs: Array<Integers> - A non-empty array of positive integers representing the clock cycles needed to finish a job.
// index: number - A positive integer that respresents the job we're interested in
// Return Value
// number - A number representing the clock cycles it takes to complete the job at index.
const sjfShort = (jobs, index) => {
  let sorted = jobs.sort((a, b) => a - b);
  const time = sorted.slice(0, index).reduce((a, b) => a + b, 0);
  return time;
};

const sjf = (jobs, index) => {
  // declare waiting time array
  var waitingTime = [];
  // set waiting time for first task to zero
  waitingTime[0] = 0;
  // declare total time array
  var totalTimeArray = [];
  var processArray = [];
  // add job value and index as an object to process array
  for (let i = 0; i < jobs.length; i++) {
    processArray.push({
      id: i,
      value: jobs[i],
    });
  }
  // sort the array in ascending order
  function sortArray(a, b) {
    return a.value - b.value;
  }
  // calculate waiting time for each process except first process
  // waiting time for first process is zero so we start to calculate from index 1
  function calculateWaitingTime(sortedArray, waitingTime) {
    for (let i = 1; i < sortedArray.length; i++) {
      waitingTime.push(sortedArray[i - 1].value + waitingTime[i - 1]);
    }
  }

  // total time taken to complete each task
  function calculateTimeForEachTask(sortedArray, totalTimeArray) {
    for (let i = 0; i < sortedArray.length; i++) {
      totalTimeArray.push({
        id: sortedArray[i].id,
        time: sortedArray[i].value + waitingTime[i],
      });
    }
  }
  // find clock cycles
  function findClockCycles(totalTimeArray, index) {
    for (let i = 0; i < totalTimeArray.length; i++) {
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
