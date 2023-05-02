import {createContext, useState} from 'react'

export const UserContext = createContext({})

export const UserProvider = ({children}) => {
    const [userId, setUserId] = useState('notYet');
    function loginUser(matricula) {
        setUserId(matricula)
        console.log("loginUser", matricula, userId)
    }
    return (
        <UserContext.Provider value={{userId, setUserId, loginUser}}>
            {children}
        </UserContext.Provider>
    )
}