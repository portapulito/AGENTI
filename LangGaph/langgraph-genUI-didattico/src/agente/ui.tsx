import React from 'react';
import { CloudSun, Thermometer, Droplets, Wind } from 'lucide-react';
import './styles.css';

const WeatherComponent = (props: { city: string }) => {
    return (
        <div className="p-4 border rounded-lg shadow-md bg-white dark:bg-gray-800">
            <div className="flex items-center gap-2 mb-2">
                <CloudSun className="w-6 h-6 text-yellow-500" />
                <h3 className="text-lg font-bold">Weather Forecast</h3>
            </div>
            <p className="mb-4">Current weather for <span className="font-semibold text-blue-500">{props.city}</span></p>

            <div className="grid grid-cols-3 gap-2 text-center text-sm">
                <div className="bg-red-50 dark:bg-red-900/20 p-3 rounded-xl flex flex-col items-center gap-2 border border-red-100 dark:border-red-800">
                    <div className="p-2 bg-red-100 dark:bg-red-800 rounded-full">
                        <Thermometer className="w-5 h-5 text-red-500 dark:text-red-300" />
                    </div>
                    <div>
                        <div className="font-bold text-gray-700 dark:text-gray-300">Temp</div>
                        <div className="text-lg font-semibold">22°C</div>
                    </div>
                </div>
                <div className="bg-blue-50 dark:bg-blue-900/20 p-3 rounded-xl flex flex-col items-center gap-2 border border-blue-100 dark:border-blue-800">
                    <div className="p-2 bg-blue-100 dark:bg-blue-800 rounded-full">
                        <Droplets className="w-5 h-5 text-blue-500 dark:text-blue-300" />
                    </div>
                    <div>
                        <div className="font-bold text-gray-700 dark:text-gray-300">Humidity</div>
                        <div className="text-lg font-semibold">45%</div>
                    </div>
                </div>
                <div className="bg-gray-50 dark:bg-gray-800 p-3 rounded-xl flex flex-col items-center gap-2 border border-gray-100 dark:border-gray-700">
                    <div className="p-2 bg-gray-200 dark:bg-gray-700 rounded-full">
                        <Wind className="w-5 h-5 text-gray-500 dark:text-gray-300" />
                    </div>
                    <div>
                        <div className="font-bold text-gray-700 dark:text-gray-300">Wind</div>
                        <div className="text-lg font-semibold">12 km/h</div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default {
    weather: WeatherComponent,
};
