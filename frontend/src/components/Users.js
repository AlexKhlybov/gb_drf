import React from 'react'


const UserItem = ({user}) => {
    return (
        <tr>
            <td>{ user.first_name }</td>
            <td>{ user.last_name }</td>
            <td>{ user.role }</td>
        </tr>
    )
}

const UserList = ({users}) => {
    return (
        <table class="table">
            <thead>
                <th scope="col">First name</th>
                <th scope="col">Last name</th>
                <th scope="col">Role</th>
            </thead>
            <tbody>
                {users.map((user) => <UserItem user={user}/>)}
            </tbody>
        </table>
    )
}

export default UserList;