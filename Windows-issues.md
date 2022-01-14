# Windows issues

## unable to start ssh-agent service, error :1058

**Reason:** service `ssh-agent` is disable in `Services`.

**Solution:** set `Manual` start for `ssh-agent` service and start the service.

Run `Windows Terminal` under `Administrator`.

Check current starting type the service:

```PowerShell
Get-Service ssh-agent | Select StartType
```

Set new starting type for the service to `Manual`:
```PowerShell
Set-Service ssh-agent -StartupType Manual
```
