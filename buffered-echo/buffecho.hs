import qualified Data.Maybe

bufferedResponse :: Maybe String -> IO ()
bufferedResponse buffer = do
    text <- getLine
    case buffer of
        Nothing -> bufferedResponse $ Just text
        Just buffer -> do
            putStrLn buffer
            bufferedResponse $ Just text

main :: IO ()
main = do
    bufferedResponse $ Nothing
