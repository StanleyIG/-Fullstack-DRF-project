import React, { Component } from 'react';
import { Link } from 'react-router-dom';

class Menu extends Component {
    render() {
        return (
            <div className="mainmenu">
                <ul className="mainmenu-style">
                    <li> <Link to='/'>Authors</Link> </li>
                    <li> <Link to='/books'>Books</Link> </li>
                    <li> <Link to='/create_book'>Create book</Link> </li>
                    <li> <Link to='/create_todo'>Create todo</Link> </li>
                    <li> <Link to='/users'>Users</Link> </li>
                    <li> <Link to='/projects'>Projects</Link> </li>
                    <li> <Link to='/todos'>ToDos</Link> </li>
                    <li>
                        {this.props.isAuth ? 
                            <Link onClick={this.props.logOut} to='#'>Logout</Link>
                            : 
                            <Link to='/login'>Login</Link>
                        }
                    </li>
                </ul>
            </div>
        );
    }
}

export default Menu;
