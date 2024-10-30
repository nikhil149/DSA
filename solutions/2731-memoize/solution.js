/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let callCount = 0;
    let cache = {};
    return function(...args) {
       if(args.join(',') in cache ){
        return cache[args.join(',')]
       } 
       callCount += 1;
       cache[args.join(',')] = fn.apply(this, args);
       return cache[args.join(',')]
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
