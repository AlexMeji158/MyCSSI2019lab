// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Use querySelector to store the div in a variable.
const Box = document.querySelector('#response-box');
const redButton = document.querySelector('#red');
const greenButton = document.querySelector('#green');
const blueButton = document.querySelector('#blue');
const clear = document.querySelector('#clear');

let list = '';

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', (e) => {
  console.log("You clicked the red button!");
  list = list + "Red ";
  Box.style.backgroundColor = 'red';
  Box.innerHTML = list;
});
greenButton.addEventListener('click', (e) => {
  console.log("You clicked the green button!");
  list = list + "Green ";
  Box.style.backgroundColor = 'green';
  Box.innerHTML = list;
});
blueButton.addEventListener('click', (e) => {
  console.log("You clicked the blue button!");
  list = list + "Blue ";
  Box.style.backgroundColor = 'blue';
  Box.innerHTML = list;
});
clear.addEventListener('click', (e) => {
  console.log("Cleared");
  list = "";
  Box.style.backgroundColor = 'white';
  Box.innerHTML = list;
});
