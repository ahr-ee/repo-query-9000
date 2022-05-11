import React from 'react';
import {Link} from 'react-router-dom';

const Header = () => {
    return (
        <div>
            <h1> github user repo query 9000 </h1>
            <ul className='nav'>
                <li>
                    <Link to='/'>query-page</Link>
                </li>
                <li>
                    <Link to='/about'>about-page</Link>
                </li>

            </ul>
        </div>
    )
}

export default Header