import React, {createContext, useContext, useReducer} from "react";

// Prepare data layer
export const StateContext = createContext();
// Provide data layer to all the app
export const StateProvider = ({ reducer, intialState, children}) =>(
    <StateContext.Provider value={useReducer(reducer,intialState)}>
        {children}
    </StateContext.Provider>
);

export const useStateValue = () => useContext(StateContext);