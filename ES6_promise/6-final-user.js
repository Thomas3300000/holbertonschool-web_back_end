import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((prom) => prom.map((prom) => ({
      status: prom.status,
      body: prom.status === 'fulfilled' ? prom.value : `Error: ${prom.reason.message}`,
    })));
}
