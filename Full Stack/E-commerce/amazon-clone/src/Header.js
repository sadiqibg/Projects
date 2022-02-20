import React from 'react';
import './Header.css';
import SearchIcon from '@mui/icons-material/Search';
import ShoppingBasketIcon from '@mui/icons-material/ShoppingBasket';
import { Link } from 'react-router-dom';

function Header() {
  return (
    <div 
    className='header'>
        <Link to= "/">
            <img
            className='header__logo' 
            src='https://pngimg.com/uploads/amazon/amazon_PNG11.png'
            alt=''
            />
        </Link>
    
        <div 
        className='header__search'>
            <input 
            className='header__searchInput'
            type='text'
            />
            <SearchIcon
            className='header__searchIcon'
            />   

        </div>

        <div 
        className='header__nav'>
            <div 
            className='header__options'>
                <span 
                className='header__optionsLineOne'>
                    Hello Guest
                </span>
                <span 
                className='header__optionsLineTwo'>
                    Sign In
                </span>

            </div>

            <div 
            className='header__options'>
                <span 
                className='header__optionsLineOne'>
                    Retuns
                </span>
                <span 
                className='header__optionsLineTwo'>
                    & Orders
                </span>
            </div>

            <div 
            className='header__options'>
                <span 
                className='header__optionsLineOne'>
                    Your
                </span>
                <span 
                className='header__optionsLineTwo'>
                    Prime
                </span>

            </div>

            <div
            className='header__optionsBasket'>
                <Link to='/checkout'>
                    <ShoppingBasketIcon/>
                    <span className='header__optionsLineTwo header__basketCount'>
                        0
                    </span>
                </Link>

            </div>
        </div>
    </div>
  )
}

export default Header;