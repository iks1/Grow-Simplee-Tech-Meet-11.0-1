import React, { useState } from 'react'
import MobileLayout from '../../Component/Layout/MobileLayout'
import {Link} from 'react-router-dom'
import Map from '../../Component/Mobile/Map'
import PackageDetails from '../../Component/Mobile/PackageDetails'


const SingleRoute = () => {

    const [routeDetails, setRouteDetails] = React.useState({
        distance: 0,
        time_required: '',
        time_to_reach: ''
    });
        
    

    const coordinates = [
        {latitude: 26.189605193409417, longitude: 91.69294796870521, status:'delivery'},
        {latitude: 26.166979228463582, longitude: 91.75049812487305, status:'pickup'},
        //{latitude: 25.5119243264636, longitude: 92.73516653680502}
    ];

/*     let statusCard = null;
    if(coordinates[1].status === 'delivery'){
        statusCard = <DeliveryStatus/>
    }else{
        statusCard = <PickupStatus/>
    } */

    return (
        <MobileLayout subHeading='Current Route'>
            <>
                <PackageDetails coordinates={coordinates[1]}/>
                <Map coordinates = {coordinates} setRouteDetails={setRouteDetails} className='flex-grow z-0'></Map>
                <div className='bottom_bar absolute inset-x-0 bottom-0 rounded-t-[12px] bg-white px-4 py-6 border border-[#D2D1CC] z-10'>
                    {/* <div className='w-full flex place-content-center pb-4'><div className='top_pill w-6 rounded-full h-[3px] bg-[#B4B4B4] '></div></div> */}
                    <div>
                        <div className='time_distance text-xl pb-1'>
                            <div className='time text-[#4CAF50] inline-block font-medium'>
                                {routeDetails.time_required}
                            </div>
                        </div>
                        <div className='info text-gs-text-gray text-[14px] pb-4'>
                            {routeDetails.distance} km • {routeDetails.time_to_reach}
                        </div>
                    </div>
                    {/* <div className='navigation_icon_parent w-12 h-12 rounded-full border border-[#D2D1CC] py-[13px] px-[13px]'> <NavigationIcon/></div> */}
                    <div className='buttons flex text-center font-semibold'>
                        <Link to='/destinationReached'  className='checklist_button rounded-full flex-1 py-3 border-[#2F2E36] border mr-2'>Reached</Link>
                        <a target="_blank" rel="noreferrer" href={'https://www.google.com/maps/dir/?api=1&destination='+ coordinates[1].latitude + '%2C' + coordinates[1].longitude} className='start_button rounded-full flex-1 py-3 bg-[#2F2E36] text-white'>Directions</a>
                    </div>
                </div>
            </>

        </MobileLayout>
    )
}

export default SingleRoute;