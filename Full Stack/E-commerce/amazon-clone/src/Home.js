import React from 'react';
import './Home.css';
import Product from './Product';

function Home() {
  return (
    <div className='home'>
        <div className='home__container'>
            <img
            className='home__image' 
            src='https://m.media-amazon.com/images/I/61aTPprCk7L._SX3000_.jpg' 
            alt=''
            />

            <div className='home__row'>
                <Product
                id ='528290143' 
                title='The Lean Startup: How Todays Entrepreneurs Use Continuous Innovation to Create Radically Successful Businesses Hardcover' 
                price='29.99' 
                image='https://images-na.ssl-images-amazon.com/images/I/81-QB7nDh4L.jpg' 
                rating= {5}/>
                <Product
                id ='528290143' 
                title='KUCCU Stand Mixer, 8.5 Qt 660W, 6-Speed Tilt-Head Food Dough Mixer, Electric Kitchen Mixer with Dough Hook, Flat Beater & Wire Whisk, Mixing Bowl' 
                price='199.99' 
                image='https://m.media-amazon.com/images/I/81CrgJhljBL._AC_SL1500_.jpg' 
                rating={5}/>
                
            </div>

            <div className='home__row'>
                <Product
                id ='528290143'  
                title='Samsung Galaxy Watch Active2 (Silicon Strap + Aluminum Bezel) Bluetooth - International' 
                price='249.75' 
                image='https://m.media-amazon.com/images/I/518qjbbuGZL._AC_SL1000_.jpg' 
                rating={4}/>
                <Product
                id ='528290143' 
                title='Echo Plus (2nd gen) Premium sound with built-in smart home hub - Charcoal' 
                price='99.99' 
                image='https://m.media-amazon.com/images/I/61S20ybHHHL._AC_SL1000_.jpg' 
                rating={3}/>
                <Product
                id ='528290143' 
                title='2021 Apple 12.9-inch iPad Pro (Wi-Fi, 256GB) - Space Grey'
                price='1,529.99' 
                image='https://m.media-amazon.com/images/I/61gQ245+F-S._AC_SL1000_.jpg' 
                rating={5}/>
                
            </div>

            <div className='home__row'>
                <Product
                id ='528290143' 
                title='SAMSUNG 49-inch Odyssey G9 Gaming Monitor | QHD, 240hz, 1000R Curved, QLED, NVIDIA G-SYNC & FreeSync' 
                price='1,878.99' 
                image='https://m.media-amazon.com/images/I/61SQz8S+fEL._AC_SL1000_.jpg' 
                rating={5}/>
            </div>
        </div>
    </div>
  )
}

export default Home