# Use luxon in React

```
$ npm install luxon
```

## Example: difference of expired_at and now

```javascript
import {DateTime, Settings} from "luxon";

Settings.defaultZoneName = "UTC";  // Set default timezone as "UTC"

const expired_at = DateTime.fromISO("2021-10-31T18:31:17");
const now = DateTime.utc();

const diff = DateTime.fromISO(expired_at).diff(now, ["days", "hours", "minutes"])

console.log(`days: ${diff.days} hours: ${diff.hours} minutes: ${diff.minutes}`)
```

`luxon` docs: https://moment.github.io/luxon/#/tour
