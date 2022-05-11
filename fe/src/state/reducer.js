const rootReducer = (state = [], action) => {
    switch (action.type) {
        case "add":
            if (state.length > 0){
                state.pop()
            }
            return state.concat(action.payload);
        default:
            return state;
    }
}

export default rootReducer