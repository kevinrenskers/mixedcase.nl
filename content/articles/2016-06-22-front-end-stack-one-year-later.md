# Our front end stack one year later
- tags: javascript

---

One year ago I wrote my third article in a series where I researched front end tools, and with all that I learned then I began to improve our front end stack at [Sling](http://www.getsling.com). It’s the big Angular app that I wrote about, which I’ve worked on for 2.5 years now. Back then we used Gulp, Bower and LESS. No modules, no ES6, barely any unit tests. We still use **Angular** 1.x, but a lot has changed in the last 12 months!

First of all, we’re now using **CommonJS modules** and **ES6 syntax** throughout the app: fat arrows, destructuring, object literal shorthands, template strings, default function parameters, etc. We’re using **Babel 6** and **Webpack** to compile all this to ES5. More specifically, we use `ng-annotate-loader` to automatically annotate our Angular modules, and `html-loader` so that we can `require` our HTML templates right into the UI Router states.

We’re no longer using Bower, instead 100% of our dependancies come from **NPM**. And we also exclusively use **NPM scripts** for running our local dev server, compiling the builds and running the tests and linter. So no more Gulp either.

We still use **LESS**, and have now combined that with PostCSS for the **autoprefixer** plugin.

Our code is linted using **ESLint**, using a slightly modified AirBnb code style. Mainly we enabled more rules. And we’ve added a ton of unit tests! We now run our tests in pure Node 6.1.0 using **Mocha**, **Chai** and **JSDom**: no browser is needed, and the code doesn’t need to go through Babel or Webpack. It’s super fast. And we’ve added **Istanbul** to get code coverage as well. We’re currently almost at 50% so definitely still have a way to go, but considering that a year ago we had almost nothing, I am very proud of the team - myself included :)

The latest addition to our stack is **SemaphoreCI**: a hosted continuous integration / deployment server. Every commit is automatically tested, we get test results right in our pull requests, and every successfully tested commit on the develop branch goes to staging, and the same for master to production. We’re now testing and deploying way more often, catching more bugs in an earlier state, and we save a lot of time and prevent errors with manual deploys. I can’t recommend this enough to everyone, and it was super simple to setup too.