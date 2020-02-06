const promiseExample = (name) => {
  return new Promise((resolve, reject) => {
    // Do anything you want
    // finishes when resolve() is called      
    setTimeout(() => {
      resolve();
     }, 3000);
  });
};

promiseExample()
  .then((res) => console.log(res))
  .catch((e) => console.log('Something went wrong!'));

console.log('hi');



const promiseExample=(name)=>{
  return new promise((resolve,reject)=>{
  setTimeout(()=> {
  },3000);
  });
  };
  
 // const promiseExample: () =>promise<any>
 // promiseExample()
 // .then((res) => console.log(res))
 // .catch(e)=>console.log('something went wrong'));
  
  
  promiseExample('Brain')
  .then(answer => 'Hello'+answer)
  .then((res)=>console.log('something went wrong!'))
  .then(()=> console.log('still going'));

